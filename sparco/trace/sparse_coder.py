import logging
import traceutil.tracer
import sparco.trace.sp

class Tracer(traceutil.tracer.Tracer):

  def wrappers(self):

    def create_spikenet(orig):
      def wrapped(self, *args, **kwargs):
        config = args[0]
        tup = (self.t, config['num_iterations'],
          config['inference_settings']['lam'],
          config['inference_settings']['maxit'])
        logging.info('Round %d: num_iterations = %d, lam = %g, maxit = %d' % tup)
        dir = "{0}_niter_{1}_lam_{2}_maxit_{3}".format(*tup)
        sn_output_path = os.path.join(self.output_path, dir)
        sparco.trace.sp.Tracer.output_path = sn_output_path
        return orig(self, *args, **kwargs)
      return wrapped

    return [create_spikenet]
