---
records:
    - id: CD968TZKF9
      kind: monograph
      title: Riemannsche Geometrie im Großen
      creators:
        - name: Detlef Gromoll
          role: author
        - name: Wilhelm Klingenberg
          role: author
        - name: Wolfgang Meyer
          role: author
      date: "1968"
      expressions:
        - key: e1
          kind: edition
          language: de
          date: "1968"
          ids:
            doi:
                - 10.1007/978-3-540-35901-2
                - 10.1007/bfb0079185
            zbl: "0155.30701"
            zbl_id: "3249638"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1968"
              ids:
                isbn:
                    - "9783540042259"
                    - "9783540359012"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1975"
              ids:
                isbn:
                    - "9783540071334"
                    - "9783540358527"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-35901-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0079185
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3249638"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: CD9T8ZFES1
      kind: preprint
      title: 'From Thomas Bayes to Big Data: On the feasibility of being a subjective Bayesian'
      creators:
        - name: Ya'acov Ritov
          role: author
      date: "2025-08-03"
      msc:
        - code: 62-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.ST
        - system: arxiv
          code: stat.TH
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2025-08-03"
          ids:
            arxiv: "2508.01642"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2508.01642"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2508.01642"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
