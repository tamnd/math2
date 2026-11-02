---
records:
    - id: RMGJK0CA3S
      kind: monograph
      title: A1-Algebraic Topology over a Field
      creators:
        - name: Fabien Morel
          role: author
      date: "2012"
      msc:
        - code: 14-02
          from: zbmath_search
        - code: 14C35
          from: zbmath_search
        - code: 14F42
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2012"
          ids:
            doi: 10.1007/978-3-642-29514-0
            zbl: "1263.14003"
            zbl_id: "6034616"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2012"
              ids:
                isbn:
                    - "9783642295133"
                    - "9783642295140"
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
          native_id: 10.1007/978-3-642-29514-0
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "6034616"
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
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
