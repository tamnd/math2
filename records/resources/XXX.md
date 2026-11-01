---
records:
    - id: XXXNME0Y8K
      kind: monograph
      title: Chaos on the Interval
      creators:
        - name: Sylvie Ruette
          role: author
      date: "2017-03-02"
      msc:
        - code: 37-02
          from: zbmath_search
        - code: "37E05"
          from: zbmath_search
        - code: 37B40
          from: zbmath_search
        - code: 37D45
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2017-03-02"
          ids:
            doi: 10.1090/ulect/067
            zbl: "1417.37029"
            zbl_id: "6704432"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2017-03-02"
              ids:
                isbn:
                    - "9781470437596"
                    - "9781470437602"
                    - "9781470429560"
              access:
                class: record
      relations:
        - kind: part_of
          to: CMK1G7XE8B
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/ulect/067
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "6704432"
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
