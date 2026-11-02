---
records:
    - id: SDQNM1N85N
      kind: monograph
      title: Multiplication of Distributions
      creators:
        - name: Jean François Colombeau
          role: author
      date: "1992"
      msc:
        - code: 65M99
          from: zbmath_search
        - code: 65N99
          from: zbmath_search
        - code: 46F10
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1992"
          ids:
            doi: 10.1007/bfb0088952
            zbl: "0815.35002"
            zbl_id: "108533"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1992"
              ids:
                isbn:
                    - "9783540562887"
                    - "9783540475101"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0088952
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "108533"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
