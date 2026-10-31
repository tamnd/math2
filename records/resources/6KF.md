---
records:
    - id: 6KFFGJ9P3K
      kind: monograph
      title: Delay Equations
      creators:
        - name: Odo Diekmann
          role: author
        - name: Sjoerd M. Verduyn Lunel
          role: author
        - name: Stephan A. van Gils
          role: author
        - name: Hanns-Otto Walther
          role: author
      date: "1995"
      expressions:
        - key: e1
          kind: edition
          date: "1995"
          ids:
            doi: 10.1007/978-1-4612-4206-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1995"
              ids:
                isbn:
                    - "9781461286967"
                    - "9781461242062"
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-4206-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 6KFS1X0MZR
      kind: preprint
      title: Identifiability of a linear dynamical reaction-diffusion system with directed interactions from the second-order statistics of a single snapshot
      creators:
        - name: Pirmin Schlicke
          role: author
      date: "2026-10-05"
      subjects:
        - system: arxiv
          code: q-bio.QM
        - system: arxiv
          code: math.PR
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-05"
          ids:
            arxiv: "2610.07341"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.07341"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
